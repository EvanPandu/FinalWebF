USE mydatabase;

CREATE TABLE user (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(80) NOT NULL,
    password VARCHAR(120) NOT NULL
);

CREATE TABLE admin (
    admin_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(80) NOT NULL,
    password VARCHAR(120) NOT NULL
);

CREATE TABLE riwayat_transaksi (
    riwayat_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(80) NOT NULL,
    quantity INT NOT NULL,
    total_price INT NOT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);

ALTER TABLE riwayat_transaksi
ADD COLUMN date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP;


CREATE TABLE wisata (
    wisata_id INT AUTO_INCREMENT PRIMARY KEY,
    tempat_wisata VARCHAR(80) NOT NULL,
    image VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    price INT NOT NULL
);

CREATE TABLE komentar (
    comment_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(80) NOT NULL,
    comment TEXT NOT NULL,
    wisata_id INT NOT NULL,
    FOREIGN KEY (wisata_id) REFERENCES wisata(wisata_id)
);

INSERT INTO user (username, password) VALUES
('fudhayl', 'fudhayl123'),
('ajul', 'ajul123'),
('rasyad', 'rasyad123');


INSERT INTO admin (username, password) VALUES
('admin1', 'admin123'),
('admin2', 'admin456');

INSERT INTO riwayat_transaksi (name, quantity, total_price, user_id, date) VALUES
('Pantai Bira', 2, 20000, 1, CURRENT_DATE),
('Gunung Latimojong', 1, 10000, 2, CURRENT_DATE),
('Banti Murung', 5, 50000, 3, CURRENT_DATE),
('Danau Tempe', 3, 30000, 1, CURRENT_DATE),
('Pulau Samalona', 4, 60000, 1, CURRENT_DATE);

INSERT INTO wisata (tempat_wisata, image, description, price) VALUES
('Pantai Bira', 'uploads/pantai_bira.jpg', 'Pantai yang terletak di Kabupaten Bulukumba ini menawarkan pasir putih dan air laut yang jernih. Pantai Bira adalah tempat yang sempurna untuk berenang, snorkeling, dan menikmati pemandangan laut yang indah.
', 50000),
('Gunung Latimojong', 'uploads/gunung_latimojong.jpg', 'Gunung tertinggi di Sulawesi Selatan ini adalah tempat favorit bagi pendaki. Puncaknya, Rantemario, menawarkan pemandangan spektakuler dari ketinggian 3.478 meter di atas permukaan laut, dengan jalur pendakian yang menantang.
', 30000),
('Pulau Samalona', 'uploads/pulau_samalona.jpg', ' Pulau kecil yang terletak di lepas pantai Makassar ini terkenal dengan keindahan bawah lautnya. Snorkeling dan diving di sini memberikan pengalaman melihat terumbu karang dan ikan-ikan tropis yang menakjubkan.
', 100000),
('Danau Tempe', 'uploads/danau_tempe.jpg', 'Danau ini terletak di Kabupaten Wajo dan dikenal dengan rumah-rumah terapung serta pemandangan alam yang menenangkan. Pengunjung dapat menikmati kegiatan memancing dan melihat burung-burung air yang eksotis.', 80000),
('Banti Murung', 'uploads/banti_murung.jpeg', 'Air terjun ini terletak di Taman Nasional Bantimurung Bulusaraung, Maros. Dikenal sebagai "Kerajaan Kupu-Kupu," tempat ini menawarkan keindahan air terjun yang memukau dan habitat kupu-kupu yang beragam.
', 70000),
('Rammang Rammang', 'uploads/rammang_rammang.jpg', 'Terletak di Kabupaten Maros, Rammang-Rammang adalah kawasan karst terbesar ketiga di dunia. Pemandangan hutan batu kapur, sungai tenang, dan gua-gua alami menjadikan tempat ini surga bagi pecinta alam dan fotografer.
', 40000);

INSERT INTO komentar (name, comment, wisata_id) VALUES
('fail', 'Tempat yang indah!', 1),
('ajul', 'Sangat coolll.', 2),
('fail', 'Tempat yang indah!', 1),
('ajul', 'Sangat hebattt.', 2),
('rasyad', 'Sangat menyenangkan.', 3);


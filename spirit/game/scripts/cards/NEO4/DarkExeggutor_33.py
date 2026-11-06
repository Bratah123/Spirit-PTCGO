from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_energy, flip_damage


card = PokemonCardDef(
    guid="e144914f-9db2-5121-854d-f31a26c788d0",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkExeggutor.Name",
    display_name="Dark Exeggutor",
    searchable_by=["Dark Exeggutor", "Stage 1", "DarkExeggutor"],
    subtypes=["Stage 1"],
    collector_number=33,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name",
    family_id=102,
    abilities=[
        Attack(
            title="Triple Headbutt",
            game_text="Flip 3 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=10),
        ),
        Attack(
            title="MAX Burst",
            game_text="Flip a number of coins equal to the number of Energy cards attached to your opponent's Pok\u00e9mon. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=flip_damage(
                coins_from=count_energy("opponent", cards=True), per_heads=20),
        ),
    ],
)

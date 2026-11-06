from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack


card = PokemonCardDef(
    guid="7a1f4378-eb90-5b3f-977f-80eecb335c6c",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hitmonlee.Name",
    display_name="Hitmonlee",
    searchable_by=["Hitmonlee", "Basic", "Hitmonlee"],
    subtypes=["Basic"],
    collector_number=81,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=106,
    abilities=[
        Attack(
            title="Smash Kick",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Stretch Kick",
            game_text="If your opponent has any Benched Pok\u00e9mon, choose 1 of them and this attack does 30 damage to it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            effect=snipe_attack(30),
        ),
    ],
)

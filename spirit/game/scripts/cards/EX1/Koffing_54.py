from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack


card = PokemonCardDef(
    guid="dcc3c10d-bb1d-5e06-a4c7-e52c11e5261c",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name",
    display_name="Koffing",
    searchable_by=["Koffing", "Basic", "Koffing"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="EX1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=109,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Double-edge",
            game_text="Koffing does 10 damage to itself.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=recoil_attack(10),
        ),
    ],
)

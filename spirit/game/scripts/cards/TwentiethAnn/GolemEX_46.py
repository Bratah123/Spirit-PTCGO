from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack


card = PokemonCardDef(
    guid="1db1a7af-5d31-5829-8500-b1496546ab3a",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GolemEX.Name",
    display_name="Golem-EX",
    searchable_by=["Golem-EX", "Basic", "EX", "GolemEX"],
    subtypes=["Basic", "EX"],
    collector_number=46,
    set_code="TwentiethAnn",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=76,
    abilities=[
        Attack(
            title="Boulder Crush",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
        ),
        Attack(
            title="Megaton Fall",
            game_text="This Pok\u00e9mon does 60 damage to itself.",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=recoil_attack(60),
        ),
    ],
)
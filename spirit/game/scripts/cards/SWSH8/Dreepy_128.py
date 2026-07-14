from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="f2804406-a2d4-5a74-bc02-78ad24e9f920",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dreepy.Name",
    display_name="Dreepy",
    searchable_by=["Dreepy", "Basic", "Fusion Strike", "Dreepy"],
    subtypes=["Basic", "Fusion Strike"],
    collector_number=128,
    set_code="SWSH8",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=885,
    abilities=[
        Attack(
            title="Infestation",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=condition_attack(no_retreat=True),
        ),
    ],
)
from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import collect_fire


card = PokemonCardDef(
    guid="1a24351e-775d-551d-90f4-e32ca29eced1",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name",
    display_name="Houndour",
    searchable_by=["Houndour", "Basic", "Houndour"],
    subtypes=["Basic"],
    collector_number=24,
    set_code="NEO2",
    rarity=Rarities.Rare,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=228,
    abilities=[
        Attack(
            title="Smog",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.POISONED, flip=True),
        ),
        Attack(
            title="Collect Fire",
            game_text="If there are any Fire Energy cards in your discard pile, choose 1 of them and attach it to Houndour.",
            cost={PokemonTypes.FIRE: 2},
            damage=20,
            effect=collect_fire,
        ),
    ],
)

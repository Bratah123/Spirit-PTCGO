from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import leech_life


card = PokemonCardDef(
    guid="76c7e448-74ec-5a9b-af71-f94148373cc8",
    key="BASE2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Venonat.Name",
    display_name="Venonat",
    searchable_by=["Venonat", "Basic", "Venonat"],
    subtypes=["Basic"],
    collector_number=63,
    set_code="BASE2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=48,
    abilities=[
        Attack(
            title="Stun Spore",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Leech Life",
            game_text="Remove a number of damage counters from Venonat equal to the damage done to the Defending Pok\u00e9mon (after applying Weakness and Resistance).",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=leech_life,
        ),
    ],
)

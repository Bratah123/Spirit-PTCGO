from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, snipe_attack


card = PokemonCardDef(
    guid="5b496852-4f8c-5145-9ffb-ed6654aa2524",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BrocksVulpix.Name",
    display_name="Brock's Vulpix",
    searchable_by=["Brock's Vulpix", "Basic", "BrocksVulpix"],
    subtypes=["Basic"],
    collector_number=37,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=37,
    abilities=[
        Attack(
            title="Hypnotic Gaze",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Fire Ring",
            game_text="If your opponent has any Benched Pok\u00e9mon, choose 1 of them and this attack does 10 damage to it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 2},
            damage=20,
            effect=snipe_attack(10, also_base=True),
        ),
    ],
)

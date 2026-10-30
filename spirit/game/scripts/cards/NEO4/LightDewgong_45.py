from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import ice_pillar


card = PokemonCardDef(
    guid="4d4f729f-b906-5605-9c4f-39c50efaf4bb",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LightDewgong.Name",
    display_name="Light Dewgong",
    searchable_by=["Light Dewgong", "Stage 1", "LightDewgong"],
    subtypes=["Stage 1"],
    collector_number=45,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seel.Name",
    family_id=86,
    abilities=[
        Attack(
            title="Freezing Breath",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed. If tails, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 2},
            damage=10,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True, tails_conditions=(SpecialConditions.ASLEEP,)),
        ),
        Attack(
            title="Ice Pillar",
            game_text="Until the end of your opponent's next turn, as long as Light Dewgong is your Active Pok\u00e9mon, prevent all damage done by attacks to your Benched Pok\u00e9mon. (Any other effects of attacks still happen.)",
            cost={PokemonTypes.WATER: 3},
            damage=40,
            effect=ice_pillar,
        ),
    ],
)

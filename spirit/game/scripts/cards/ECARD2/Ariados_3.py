from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import GlueySlimePassive


card = PokemonCardDef(
    guid="370bd3e7-60bc-57b3-b279-5022090621a8",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ariados.Name",
    display_name="Ariados",
    searchable_by=["Ariados", "Stage 1", "Ariados"],
    subtypes=["Stage 1"],
    collector_number=3,
    set_code="ECARD2",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spinarak.Name",
    family_id=167,
    abilities=[
        Ability(
            title="Gluey Slime",
            game_text="As long as Ariados is in play, each player must pay an additional Colorless to retreat his or her Active Pok\u00e9mon. Gluey Slime can't make a player pay more than an additional Colorless to retreat a Pok\u00e9mon, even if there is more than 1 Ariados in play.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=GlueySlimePassive(),
        ),
        Attack(
            title="Spider Force",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 10 more damage. If tails, this attack does 20 damage and the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=condition_attack(
                flip=True, heads_bonus_damage=10,
                tails_conditions=(SpecialConditions.PARALYZED,),
            ),
        ),
    ],
)

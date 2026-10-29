from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.passives_common import boost_own_next_turn


card = PokemonCardDef(
    guid="a31e42b5-278a-524c-bd41-cf606835636e",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Metagross.Name",
    display_name="Metagross",
    searchable_by=["Metagross", "Stage 2", "Metagross"],
    subtypes=["Stage 2"],
    collector_number=95,
    set_code="SM7",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name",
    family_id=374,
    abilities=[
        Ability(
            title="Extend",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, your turn does not end when you play Steven's Resolve.",
            ability_type=AbilityTypes.POKE_ABILITY,
        ),
        Attack(
            title="Meteor Mash",
            game_text="During your next turn, this Pok\u00e9mon's Meteor Mash attack does 60 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1},
            damage=60,
            # STUB: attack effect not implemented
            effect=boost_own_next_turn(60, attack_title='Meteor Mash'),
        ),
    ],
)
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, recoil_attack

from spirit.game.card_effects.attacks_common import damage_per, recoil_attack


def _opponent_prizes_taken_last_turn(ctx):
    return ctx.session.turn_state.prizes_taken_last_turn.get(ctx.opponent_id, 0)


card = PokemonCardDef(
    guid="84cb8e69-31ff-5d86-90d2-a31a2479c23b",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machamp.Name",
    display_name="Machamp",
    searchable_by=["Machamp", "Stage 2", "Machamp"],
    subtypes=["Stage 2"],
    collector_number=65,
    set_code="SM2",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name",
    family_id=66,
    abilities=[
        Attack(
            title="Settle the Score",
            game_text="This attack does 80 more damage for each Prize card your opponent took on their last turn.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=20,
            damage_operator="+",
            effect=damage_per(_opponent_prizes_taken_last_turn, 80, base=20),
        ),
        Attack(
            title="Submission",
            game_text="This Pok\u00e9mon does 30 damage to itself.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=150,
            effect=recoil_attack(30),
        ),
    ],
)
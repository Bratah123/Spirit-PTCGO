from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if


def _stakeout_bonus(ctx):
    active = ctx.opponent_active()
    if active is None:
        return False
    turn_state = ctx.session.turn_state
    return turn_state.became_active_turn.get(active.entity_id) == turn_state.turn_number - 1


card = PokemonCardDef(
    guid="e70c910b-dcf4-5666-9b5d-db5ece37d83f",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gumshoos.Name",
    display_name="Gumshoos",
    searchable_by=["Gumshoos", "Stage 1", "Gumshoos"],
    subtypes=["Stage 1"],
    collector_number=118,
    set_code="CZ",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Yungoos.Name",
    family_id=734,
    abilities=[
        Attack(
            title="Stakeout Headbutt",
            game_text="If your opponent's Active Pok\u00e9mon moved from the Bench to the Active Spot during your opponent's last turn, this attack does 120 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=bonus_if(_stakeout_bonus, 120),
        ),
        Attack(
            title="Lunge Out",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
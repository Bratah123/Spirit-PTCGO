from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage, bonus_if
from spirit.game.content.definitions import def_for


def _evolved_from_meowth_this_turn(ctx):
    ts = ctx.session.turn_state
    me = ctx.attacker
    if ts.entered_play_turn.get(me.entity_id) != ts.turn_number:
        return False
    return any(getattr(def_for(c.archetype_id), "display_name", "") == "Meowth" for c in me.children)


card = PokemonCardDef(
    guid="e9f16493-9cfa-5806-a287-275727c28cd1",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Persian.Name",
    display_name="Persian",
    searchable_by=["Persian", "Stage 1", "Persian"],
    subtypes=["Stage 1"],
    collector_number=89,
    set_code="XY11",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name",
    family_id=52,
    abilities=[
        Attack(
            title="Raid",
            game_text="If this Pok\u00e9mon evolved from Meowth during this turn, this attack does 30 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=bonus_if(_evolved_from_meowth_this_turn, 30),
        ),
        Attack(
            title="Fury Swipes",
            game_text="Flip 3 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=30),
        ),
    ],
)
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import lock_defender_attacks
from spirit.game.card_effects.passives_common import retreat_free_when
from spirit.game.session.effects import is_evolution_pokemon


async def leg_quake(ctx):
    """100. If the Defending Pokemon is an Evolution Pokemon, it can't
    attack during your opponent's next turn."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None and is_evolution_pokemon(defender):
        lock_defender_attacks(ctx)


card = PokemonCardDef(
    guid="ab517795-5f1e-5a54-aca9-c3bbd687d09f",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Metagross.Name",
    display_name="Metagross",
    searchable_by=["Metagross", "Stage 2", "Metagross"],
    subtypes=["Stage 2"],
    collector_number=118,
    set_code="SWSH4",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name",
    family_id=374,
    abilities=[
        Ability(
            title="Levitation Field",
            game_text="Your Pokémon in play have no Retreat Cost.",
            passive=retreat_free_when(lambda p, c: p.owning_player_id == c.owning_player_id),
        ),
        Attack(
            title="Leg Quake",
            game_text="If the Defending Pokémon is an Evolution Pokémon, it can't attack during your opponent's next turn.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=leg_quake,
        ),
    ],
)

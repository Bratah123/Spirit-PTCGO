from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.content.definitions import def_for


def _team(p, team):
    name = getattr(def_for(p.archetype_id), "display_name", "") or ""
    return name.startswith("Team " + team + "'s ")


def _magma_switch_condition(board, player_id, pokemon=None):
    mons = board.pokemon_in_play(player_id)
    return any(_team(p, "Magma") for p in mons) and any(
        is_basic_energy_card(e) for p in mons for e in board.attached_energies(p))


async def _magma_switch(ctx):
    """Move a basic Energy from 1 of your Pokemon to 1 of your Team Magma Pokemon."""
    mons = ctx.my_pokemon_in_play()
    await ctx.move_energy_freely(mons, [p for p in mons if _team(p, "Magma")],
                                 predicate=is_basic_energy_card, max_count=1,
                                 prompt="Move a basic Energy to a Team Magma Pokémon")


card = PokemonCardDef(
    guid="6e8067ee-5346-5caf-9acb-1d9b0f02f058",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasClaydol.Name",
    display_name="Team Magma's Claydol",
    searchable_by=["Team Magma's Claydol", "Stage 1", "TeamMagmasClaydol"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="TATM",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasBaltoy.Name",
    family_id=343,
    abilities=[
        Ability(
            title="Magma Switch",
            game_text="Once during your turn (before your attack), you may move a basic Energy from 1 of your Pok\u00e9mon to 1 of your Team Magma Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_magma_switch_condition,
            effect=_magma_switch,
        ),
        Attack(
            title="Power Beam",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
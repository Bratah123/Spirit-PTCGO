from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.session.effects import plasma_energy_attached


def _plasma_transfer_condition(board, player_id, pokemon=None):
    mine = board.pokemon_in_play(player_id)
    return len(mine) >= 2 and any(plasma_energy_attached(p) for p in mine)


async def _plasma_transfer(ctx):
    """As often as you like during your turn, move a Plasma Energy attached to
    1 of your Pokemon to another of your Pokemon."""
    mine = ctx.my_pokemon_in_play()
    pool = [e for p in mine for e in plasma_energy_attached(p)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Plasma Energy to move")
    if not picks:
        return
    energy = picks[0]
    dests = [p for p in mine if p is not energy.parent]
    if dests:
        target = dests[0] if len(dests) == 1 else await ctx.choose_pokemon(dests, "Move it to which Pokémon?")
        await ctx.move_energy(energy, target or dests[0])


card = PokemonCardDef(
    guid="146346cf-5904-5fee-87ac-9e4c2969520d",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PorygonZ.Name",
    display_name="Porygon-Z",
    searchable_by=["Porygon-Z", "Stage 2", "Team Plasma", "PorygonZ"],
    subtypes=["Stage 2", "Team Plasma"],
    collector_number=84,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon2.Name",
    family_id=137,
    abilities=[
        Ability(
            title="Plasma Transfer",
            game_text="As often as you like during your turn (before your attack), you may move a Plasma Energy attached to 1 of your Pok\u00e9mon to another of your Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.UNLIMITED,
            condition=_plasma_transfer_condition,
            effect=_plasma_transfer,
        ),
        Attack(
            title="Tri Attack",
            game_text="Flip 3 coins. This attack does 50 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="x",
            effect=flip_damage(3, per_heads=50),
        ),
    ],
)
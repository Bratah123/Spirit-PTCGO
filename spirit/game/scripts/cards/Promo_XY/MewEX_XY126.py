from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.session.passives import Passive
from spirit.game.content.definitions import def_for, Attack as _AttackDef


class VersatilePassive(Passive):
    """Versatile: this Pokemon can use the attacks of any Pokemon in play
    (both sides); Energy costs still apply."""

    def granted_attacks(self, board, pokemon, carrier):
        if carrier is not pokemon:
            return []
        attacks = []
        for pid in board.player_ids:
            for other in board.pokemon_in_play(pid):
                if other is pokemon:
                    continue
                for ability in getattr(def_for(other.archetype_id), "abilities", None) or []:
                    if isinstance(ability, _AttackDef):
                        attacks.append(ability)
        return attacks


async def _replace(ctx):
    """Move as many Energy attached to your Pokemon to your other Pokemon in any way you like."""
    mine = ctx.my_pokemon_in_play()
    if len(mine) < 2:
        return
    await ctx.move_energy_freely(mine, mine, prompt="Choose an Energy to move")


card = PokemonCardDef(
    guid="cb8ee538-8659-505f-993f-f5339c2946e6",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MewEX.Name",
    display_name="Mew-EX",
    searchable_by=["Mew-EX", "Basic", "EX", "MewEX"],
    subtypes=["Basic", "EX"],
    collector_number=126,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=151,
    abilities=[
        Ability(
            title="Versatile",
            game_text="This Pok\u00e9mon can use the attacks of any Pok\u00e9mon in play (both yours and your opponent's). (You still need the necessary Energy to use each attack.)",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=VersatilePassive(),
        ),
        Attack(
            title="Replace",
            game_text="Move as many Energy attached to your Pok\u00e9mon to your other Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=_replace,
        ),
    ],
)
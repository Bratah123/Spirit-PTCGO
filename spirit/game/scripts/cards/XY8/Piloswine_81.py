from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import gust_attack
from spirit.game.content.definitions import def_for
from spirit.game.session.passives import effective_retreat_cost


async def _gathering_footsteps(ctx):
    """30+; 10 more per Colorless in the Retreat Costs of your Swinub, Piloswine, and Mamoswine."""
    n = sum(effective_retreat_cost(ctx.board, p) for p in ctx.my_pokemon_in_play()
            if getattr(def_for(p.archetype_id), "display_name", None) in ("Swinub", "Piloswine", "Mamoswine"))
    await ctx.deal_damage(ctx.ability.damage + 10 * n)


card = PokemonCardDef(
    guid="2a13d97e-e6fa-57d7-ba7f-c416813adef3",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Piloswine.Name",
    display_name="Piloswine",
    searchable_by=["Piloswine", "Stage 1", "Piloswine"],
    subtypes=["Stage 1"],
    collector_number=81,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swinub.Name",
    family_id=220,
    abilities=[
        Attack(
            title="Push Down",
            game_text="Your opponent switches his or her Active Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=gust_attack(opponent_chooses=True),
        ),
        Attack(
            title="Gathering Footsteps",
            game_text="This attack does 10 more damage for each Colorless in the Retreat Cost of your Swinub, Piloswine, and Mamoswine.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=_gathering_footsteps,
        ),
    ],
)
from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.content.definitions import def_for


async def _turbo_assault(ctx):
    """60; attach an Energy card from your discard pile to 1 of your Pokemon."""
    await ctx.deal_damage()
    pool = [c for c in ctx.discard_pile() if is_energy_card(c)]
    if not pool:
        return
    pick = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose an Energy card")
    mine = ctx.my_pokemon_in_play()
    target = mine[0] if len(mine) == 1 else await ctx.choose_pokemon(mine, "Attach to which Pokémon?")
    if pick and target is not None:
        await ctx.attach_energy(pick[0], target)


def _is_ex(p):
    return "EX" in (getattr(def_for(p.archetype_id), "subtypes", None) or [])


card = PokemonCardDef(
    guid="40e40b77-e00b-521a-ad31-9875c2ea2b7b",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Garchomp.Name",
    display_name="Garchomp",
    searchable_by=["Garchomp", "Stage 2", "Garchomp"],
    subtypes=["Stage 2"],
    collector_number=70,
    set_code="XY9",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gabite.Name",
    family_id=443,
    abilities=[
        Attack(
            title="Turbo Assault",
            game_text="Attach an Energy card from your discard pile to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=60,
            effect=_turbo_assault,
        ),
        Attack(
            title="Bite Off",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon-EX, this attack does 80 more damage.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=80,
            damage_operator="+",
            effect=bonus_if(lambda ctx: ctx.opponent_active() is not None and _is_ex(ctx.opponent_active()), 80),
        ),
    ],
)
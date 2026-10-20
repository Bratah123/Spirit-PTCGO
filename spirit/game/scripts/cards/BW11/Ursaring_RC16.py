from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.content.definitions import def_for
from spirit.game.card_effects.pokemon import is_energy_card


async def _picnic_weather(ctx):
    """Put a Teddiursa from your discard pile onto your Bench. Then, attach an
    Energy card from your discard pile to that Pokemon."""
    teddy = [c for c in ctx.discard_pile()
             if getattr(def_for(c.archetype_id), "display_name", "") == "Teddiursa"]
    if not teddy:
        return
    picks = await ctx.choose_cards(teddy, 1, minimum=1, prompt="Choose a Teddiursa to bench")
    if not picks or not await ctx.bench_pokemon(picks[0]):
        return
    benched = next((p for p in ctx.my_bench() if p.entity_id == picks[0].entity_id or picks[0] in p.children), None)
    energy = [c for c in ctx.discard_pile() if is_energy_card(c)]
    if benched is None or not energy:
        return
    e = await ctx.choose_cards(energy, 1, minimum=1, prompt="Choose an Energy card to attach")
    if e:
        await ctx.attach_energy(e[0], benched)


card = PokemonCardDef(
    guid="34a0aa9e-6194-5859-90bd-6843797ddf42",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ursaring.Name",
    display_name="Ursaring",
    searchable_by=["Ursaring", "Stage 1", "Ursaring"],
    subtypes=["Stage 1"],
    collector_number=131,
    set_code="BW11",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Teddiursa.Name",
    family_id=216,
    abilities=[
        Attack(
            title="Picnic Weather",
            game_text="Put a Teddiursa from your discard pile onto your Bench. Then, attach an Energy card from your discard pile to that Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=_picnic_weather,
        ),
        Attack(
            title="Fury Swipes",
            game_text="Flip 3 coins. This attack does 50 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=50,
            damage_operator="x",
            effect=flip_damage(3, per_heads=50),
        ),
    ],
)
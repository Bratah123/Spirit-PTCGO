from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_lightning_energy, energy_provides_type
from spirit.game.card_effects.support_common import search_attach_energy


async def dynamic_spark(ctx):
    """You may discard any amount of Lightning Energy from this Pokemon;
    60 damage for each card discarded this way."""
    attached = [
        e for e in ctx.attached_energies(ctx.attacker)
        if energy_provides_type(e, PokemonTypes.LIGHTNING.value)
    ]
    picks = []
    if attached:
        picks = await ctx.choose_cards(
            attached, len(attached), minimum=0,
            prompt="Discard any amount of Lightning Energy from this Pokémon.",
        )
        if picks:
            await ctx.discard_cards(picks)
    await ctx.deal_damage(60 * len(picks))


card = PokemonCardDef(
    guid="d2cd69b4-9c28-5ef4-9bf2-4b0f12c2cf89",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RaichuV.Name",
    display_name="Raichu V",
    searchable_by=["Raichu V", "Basic", "V", "RaichuV"],
    subtypes=["Basic", "V"],
    collector_number=158,
    set_code="SWSH9",
    rarity=Rarities.RareUltra,
    hp=200,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=26,
    abilities=[
        Attack(
            title="Fast Charge",
            game_text="If you go first, you can use this attack during your first turn. Search your deck for a Lightning Energy card and attach it to this Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.LIGHTNING: 1},
            usable_first_turn=True,
            effect=search_attach_energy(predicate=is_lightning_energy, count=1, to_self=True),
        ),
        Attack(
            title="Dynamic Spark",
            game_text="You may discard any amount of Lightning Energy from your Pok\u00e9mon. This attack does 60 damage for each card you discarded in this way.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=60,
            damage_operator="x",
            effect=dynamic_spark,
        ),
    ],
)
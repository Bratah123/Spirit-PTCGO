from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.passives_common import is_in_active_spot


async def sky_heal(ctx):
    """40. If Latios is on your Bench, heal 20 from this Pokémon."""
    await ctx.deal_damage()
    if any(
        p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Latios"
        for p in ctx.my_bench()
    ):
        await ctx.heal(20, ctx.attacker)


card = PokemonCardDef(
    guid="ce7ef366-c12c-5bc2-8196-d2e792004a98",
    key="DV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latias.Name",
    display_name="Latias",
    searchable_by=["Latias", "Basic", "Latias"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="DV1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DRAGON,
    family_id=380,
    abilities=[
        Attack(
            title="Energy Assist",
            game_text="Attach a basic Energy card from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=attach_from_discard(
                predicate=is_basic_energy_card, count=1,
                target=lambda p: not is_in_active_spot(p),
                prompt="Choose a basic Energy card to attach to a Benched Pokémon",
            ),
        ),
        Attack(
            title="Sky Heal",
            game_text="If Latios is on your Bench, heal 20 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.PSYCHIC: 1},
            damage=40,
            effect=sky_heal,
        ),
    ],
)

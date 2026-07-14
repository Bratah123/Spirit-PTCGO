from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_energy_card


def _is_fighting_energy(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_energy_card(card) and PokemonTypes.FIGHTING.value in types


async def stone_gift(ctx):
    """Attach a Fighting Energy card from your hand to 1 of your Pokémon.
    If you do, heal 120 damage from that Pokémon."""
    energies = [c for c in ctx.hand() if _is_fighting_energy(c)]
    if not energies:
        return
    picked = await ctx.choose_cards(
        energies, 1, minimum=1, prompt="Choose a Fighting Energy card to attach"
    )
    if not picked:
        return
    target = await ctx.choose_pokemon(
        ctx.my_pokemon_in_play(), "Choose a Pokémon to attach the Fighting Energy to"
    )
    if target is None:
        return
    await ctx.attach_energy(picked[0], target)
    await ctx.heal(120, target)

card = PokemonCardDef(
    guid="6cbb866b-c7db-52cf-a07c-eebaebb46086",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.StonjournerVMAX.Name",
    display_name="Stonjourner VMAX",
    searchable_by=["Stonjourner VMAX", "VMAX", "StonjournerVMAX"],
    subtypes=["VMAX"],
    collector_number=116,
    set_code="SWSH1",
    rarity=Rarities.RareHoloVMAX,
    hp=330,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.StonjournerV.Name",
    family_id=874,
    abilities=[
        Attack(
            title="Stone Gift",
            game_text="Attach a Fighting Energy card from your hand to 1 of your Pok\u00e9mon. If you do, heal 120 damage from that Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=stone_gift,
        ),
        Attack(
            title="Max Rockfall",
            cost={PokemonTypes.FIGHTING: 3},
            damage=200,
        ),
    ],
)
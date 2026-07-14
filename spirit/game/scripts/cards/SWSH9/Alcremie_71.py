from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import AttrID, CardType, PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_special_energy


async def rainbow_flavor(ctx):
    """10, +40 for each distinct type of basic Energy attached to all of your Pokemon."""
    types = set()
    for pokemon in ctx.my_pokemon_in_play():
        for energy in ctx.attached_energies(pokemon):
            if energy.get_attribute(AttrID.CARD_TYPE) == CardType.ENERGY.value \
                    and not is_special_energy(energy):
                types.update(energy.get_attribute(AttrID.POKEMON_TYPES) or [])
    await ctx.deal_damage(10 + 40 * len(types))

card = PokemonCardDef(
    guid="37d5a9ae-c2a9-5bc2-9ba0-da81317e2bca",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Alcremie.Name",
    display_name="Alcremie",
    searchable_by=["Alcremie", "Stage 1", "Alcremie"],
    subtypes=["Stage 1"],
    collector_number=71,
    set_code="SWSH9",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Milcery.Name",
    family_id=868,
    abilities=[
        # Marker ability: the Caf\u00e9 Master supporter script checks for it on
        # the Active before applying its "Your turn ends." clause.
        Ability(
            title="Additional Order",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, your turn does not end when you use Caf\u00e9 Master.",
        ),
        Attack(
            title="Rainbow Flavor",
            game_text="This attack does 40 more damage for each type of basic Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=rainbow_flavor,
        ),
    ],
)
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations, is_pokemon_v
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.card_effects.trainers import is_basic_energy_card


async def starbirth(ctx):
    """VSTAR Power: search your deck for up to 2 cards and put them into your hand."""
    picks = await ctx.search_deck(
        None, count=2, minimum=0, prompt="Choose up to 2 cards to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="b3e4bb6e-c548-5a90-9649-ba1d0f9a6d52",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ArceusVSTAR.Name",
    display_name="Arceus VSTAR",
    searchable_by=["Arceus VSTAR", "VSTAR", "ArceusVSTAR"],
    subtypes=["VSTAR"],
    collector_number=123,
    set_code="SWSH9",
    rarity=Rarities.RareHoloVSTAR,
    hp=280,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ArceusV.Name",
    family_id=493,
    abilities=[
        Ability(
            title="Starbirth",
            game_text="During your turn, you may search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck. (You can't use more than 1 VSTAR Power in a game.)",
            activation=Activations.ONCE_PER_TURN,
            vstar=True,
            effect=starbirth,
        ),
        Attack(
            title="Trinity Nova",
            game_text="Search your deck for up to 3 basic Energy cards and attach them to your Pok\u00e9mon V in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=200,
            effect=search_attach_energy(
                is_basic_energy_card, count=3,
                target_pred=lambda p: is_pokemon_v(p.archetype_id),
            ),
        ),
    ],
)
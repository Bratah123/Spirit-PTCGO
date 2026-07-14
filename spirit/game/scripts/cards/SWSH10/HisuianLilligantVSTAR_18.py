from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_pokemon_card
from spirit.game.card_effects.trainers import is_grass_energy_card


def _is_grass_pokemon(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_pokemon_card(card) and PokemonTypes.GRASS.value in types


def _is_grass_pokemon_or_energy(card):
    return _is_grass_pokemon(card) or is_grass_energy_card(card)


async def star_perfume(ctx):
    if await ctx.ask_yes_no(
        "Search your deck for up to 5 in any combination of Grass "
        "Pokémon and Grass Energy cards?"
    ):
        picks = await ctx.search_deck(
            _is_grass_pokemon_or_energy, count=5, minimum=0,
            prompt="Choose up to 5 Grass Pokémon and Grass Energy cards.",
        )
        await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()


async def parallel_spin(ctx):
    energies = ctx.attached_energies(ctx.source)
    bonus = 0
    if energies:
        picks = await ctx.choose_cards(
            energies, 1, minimum=0,
            prompt="Put an Energy attached to this Pokémon into your hand?",
        )
        if picks:
            await ctx.put_in_hand(picks, reveal=False)
            bonus = 100
    await ctx.deal_damage(130 + bonus)


card = PokemonCardDef(
    guid="4816d51d-d3b7-5122-b7ce-93e30fbdbd30",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianLilligantVSTAR.Name",
    display_name="Hisuian Lilligant VSTAR",
    searchable_by=["Hisuian Lilligant VSTAR", "VSTAR", "HisuianLilligantVSTAR"],
    subtypes=["VSTAR"],
    collector_number=18,
    set_code="SWSH10",
    rarity=Rarities.RareHoloVSTAR,
    hp=260,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.VSTAR,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianLilligantV.Name",
    family_id=549,
    abilities=[
        Ability(
            title="Star Perfume",
            game_text="During your turn, you may search your deck for up to 5 in any combination of Grass Pok\u00e9mon and Grass Energy cards, reveal them, and put them into your hand. Then, shuffle your deck. (You can't use more than 1 VSTAR Power in a game.)",
            vstar=True,
            effect=star_perfume,
        ),
        Attack(
            title="Parallel Spin",
            game_text="You may put an Energy attached to this Pok\u00e9mon into your hand. If you do, this attack does 100 more damage.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            damage_operator="+",
            effect=parallel_spin,
        ),
    ],
)
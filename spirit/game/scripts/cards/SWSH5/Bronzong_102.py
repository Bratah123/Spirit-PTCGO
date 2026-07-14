from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type


def _metal_transfer_condition(board, player_id, pokemon):
    pkmn = board.pokemon_in_play(player_id)
    if len(pkmn) < 2:
        return False
    return any(
        energy_provides_type(e, PokemonTypes.METAL)
        for p in pkmn for e in board.attached_energies(p)
    )


async def metal_transfer(ctx):
    pool = [
        (e, p) for p in ctx.my_pokemon_in_play()
        for e in ctx.attached_energies(p)
        if energy_provides_type(e, PokemonTypes.METAL)
    ]
    if not pool:
        return
    picked = await ctx.choose_cards(
        [e for e, _ in pool], 1, prompt="Choose a Metal Energy to move"
    )
    if not picked:
        return
    energy = picked[0]
    holder = next(p for e, p in pool if e is energy)
    targets = [p for p in ctx.my_pokemon_in_play() if p is not holder]
    if not targets:
        return
    target = await ctx.choose_pokemon(targets, "Choose a Pokémon to move the Energy to")
    if target is not None:
        await ctx.move_energy(energy, target)


card = PokemonCardDef(
    guid="7df7a5df-48ff-5e06-a961-f5e068a186df",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzong.Name",
    display_name="Bronzong",
    searchable_by=["Bronzong", "Stage 1", "Bronzong"],
    subtypes=["Stage 1"],
    collector_number=102,
    set_code="SWSH5",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name",
    family_id=436,
    abilities=[
        Ability(
            title="Metal Transfer",
            game_text="As often as you like during your turn, you may move a Metal Energy from 1 of your Pok\u00e9mon to another of your Pok\u00e9mon.",
            activation=Activations.UNLIMITED,
            condition=_metal_transfer_condition,
            effect=metal_transfer,
        ),
        Attack(
            title="Zen Headbutt",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
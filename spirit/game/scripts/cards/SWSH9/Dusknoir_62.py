from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_special_energy


def _special_transfer_condition(board, player_id, pokemon):
    pkmn = board.pokemon_in_play(player_id)
    if len(pkmn) < 2:
        return False
    return any(is_special_energy(e) for p in pkmn for e in board.attached_energies(p))


async def special_transfer(ctx):
    pool = [
        (e, p) for p in ctx.my_pokemon_in_play()
        for e in ctx.attached_energies(p)
        if is_special_energy(e)
    ]
    if not pool:
        return
    picked = await ctx.choose_cards(
        [e for e, _ in pool], 1, prompt="Choose a Special Energy to move"
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
    guid="1ec71624-7a88-544d-9d72-106cf636d8b1",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dusknoir.Name",
    display_name="Dusknoir",
    searchable_by=["Dusknoir", "Stage 2", "Dusknoir"],
    subtypes=["Stage 2"],
    collector_number=62,
    set_code="SWSH9",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dusclops.Name",
    family_id=355,
    abilities=[
        Ability(
            title="Special Transfer",
            game_text="As often as you like during your turn, you may move a Special Energy from 1 of your Pok\u00e9mon to another of your Pok\u00e9mon.",
            activation=Activations.UNLIMITED,
            condition=_special_transfer_condition,
            effect=special_transfer,
        ),
        Attack(
            title="Devour Soul",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
    ],
)
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import mega_thrash, scram_passive


card = PokemonCardDef(
    guid="181398b6-b27e-58c6-83d7-495697601bec",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BrocksPrimeape.Name",
    display_name="Brock's Primeape",
    searchable_by=["Brock's Primeape", "Stage 1", "BrocksPrimeape"],
    subtypes=["Stage 1"],
    collector_number=35,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.BrocksMankey.Name",
    family_id=57,
    abilities=[
        Ability(
            title="Scram",
            game_text="If Brock's Primeape ever has exactly 10 HP left, shuffle it and all cards attached to it into your deck. This power stops working while Brock's Primeape is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            passive=scram_passive,
        ),
        Attack(
            title="Mega Thrash",
            game_text="Brock's Primeape does 20 damage to itself. If there is a Stadium card in play, discard it.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=60,
            effect=mega_thrash,
        ),
    ],
)

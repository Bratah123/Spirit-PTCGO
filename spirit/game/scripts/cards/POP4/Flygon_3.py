from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import levitate_any_energy_passive, magma_ring_no_retreat


card = PokemonCardDef(
    guid="cdf81a41-7dbd-520f-8e67-409f7e3c88d9",
    key="POP4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flygon.Name",
    display_name="Flygon",
    searchable_by=["Flygon", "Stage 2", "Flygon"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="POP4",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name",
    family_id=330,
    abilities=[
        Ability(
            title="Levitate",
            game_text="As long as Flygon has any Energy attached to it, the Retreat Cost for Flygon is 0.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=levitate_any_energy_passive(),
            effect=None,
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Sand Pit",
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=70,
            effect=magma_ring_no_retreat(),
        ),
    ],
)

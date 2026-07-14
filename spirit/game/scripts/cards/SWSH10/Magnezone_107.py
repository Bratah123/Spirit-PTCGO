from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_metal_energy_card
from spirit.game.card_effects.support_common import look_top_attach_energy

card = PokemonCardDef(
    guid="02797afc-381d-566d-bdaa-10efd93d833b",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magnezone.Name",
    display_name="Magnezone",
    searchable_by=["Magnezone", "Stage 2", "Magnezone"],
    subtypes=["Stage 2"],
    collector_number=107,
    set_code="SWSH10",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name",
    family_id=81,
    abilities=[
        Ability(
            title="Giga Magnet",
            game_text="Once during your turn, you may look at the top 6 cards of your deck and attach any number of Metal Energy cards you find there to your Pok\u00e9mon in any way you like. Shuffle the other cards back into your deck.",
            activation=Activations.ONCE_PER_TURN,
            effect=look_top_attach_energy(6, predicate=is_metal_energy_card),
        ),
        Attack(
            title="Power Beam",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
    ],
)
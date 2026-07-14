from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_grass_energy_card
from spirit.game.card_effects.support_common import search_attach_energy

card = PokemonCardDef(
    guid="20fcc91d-1cb0-5fbd-97a6-e2120e2cc9a2",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rillaboom.Name",
    display_name="Rillaboom",
    searchable_by=["Rillaboom", "Stage 2", "Rillaboom"],
    subtypes=["Stage 2"],
    collector_number=197,
    set_code="SWSH3",
    rarity=Rarities.RareSecret,
    hp=170,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Thwackey.Name",
    family_id=812,
    abilities=[
        Ability(
            title="Voltage Beat",
            game_text="Once during your turn, you may search your deck for up to 2 Grass Energy cards and attach them to 1 of your Pok\u00e9mon. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            effect=search_attach_energy(predicate=is_grass_energy_card, count=2, distribute=False),
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.GRASS: 3, PokemonTypes.COLORLESS: 1},
            damage=140,
        ),
    ],
)
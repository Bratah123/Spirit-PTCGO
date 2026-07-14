from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import look_top_attach_energy
from spirit.game.card_effects.trainers import is_basic_energy_card

charging_trumpet = look_top_attach_energy(
    3, predicate=is_basic_energy_card, rest="shuffle", distribute=True, minimum=0
)

card = PokemonCardDef(
    guid="81affd0a-3e81-56d8-acc0-3a0eb67c3c9f",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Trumbeak.Name",
    display_name="Trumbeak",
    searchable_by=["Trumbeak", "Stage 1", "Trumbeak"],
    subtypes=["Stage 1"],
    collector_number=144,
    set_code="SWSH4",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pikipek.Name",
    family_id=731,
    abilities=[
        Ability(
            title="Charging Trumpet",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may look at the top 3 cards of your deck and attach any number of basic Energy cards you find there to your Pok\u00e9mon in any way you like. Shuffle the other cards back into your deck.",
            trigger=Triggers.ON_EVOLVE,
            effect=charging_trumpet,
        ),
        Attack(
            title="Drill Peck",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
    ],
)
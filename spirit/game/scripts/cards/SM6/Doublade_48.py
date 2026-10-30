from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm6 import curse_of_the_blade

card = PokemonCardDef(
    guid="46ed545f-af43-56fd-8a97-5b50ae3a418e",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Doublade.Name",
    display_name="Doublade",
    searchable_by=["Doublade", "Stage 1", "Doublade"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Honedge.Name",
    family_id=679,
    abilities=[
        Attack(
            title="Curse of the Blade",
            game_text="Put 3 damage counters on each of your opponent's Pok\u00e9mon that has a Pok\u00e9mon Tool card attached to it.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=curse_of_the_blade,
        ),
    ],
)

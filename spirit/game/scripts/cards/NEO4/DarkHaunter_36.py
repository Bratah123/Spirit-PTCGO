from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import call_back, call_back_condition, surround


card = PokemonCardDef(
    guid="6993c7be-1f7b-5fb1-8cda-adedaf6e2e9c",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkHaunter.Name",
    display_name="Dark Haunter",
    searchable_by=["Dark Haunter", "Stage 1", "DarkHaunter"],
    subtypes=["Stage 1"],
    collector_number=36,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gastly.Name",
    family_id=92,
    abilities=[
        Attack(
            title="Call Back",
            game_text="Put a Baby Pok\u00e9mon or Basic Pok\u00e9mon card from your opponent's discard pile onto his or her Bench. Put 1 damage counter on that Pok\u00e9mon. (You can't use this attack if your Bench is full.)",
            cost={PokemonTypes.PSYCHIC: 1},
            condition=call_back_condition,
            effect=call_back,
        ),
        Attack(
            title="Surround",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Asleep. If tails, the Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=20,
            effect=surround,
        ),
    ],
)

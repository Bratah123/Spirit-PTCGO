from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import lightning_bolt, lightning_rod


card = PokemonCardDef(
    guid="531c9b8c-8446-5459-8543-447297314392",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electabuzz.Name",
    display_name="Electabuzz",
    searchable_by=["Electabuzz", "Basic", "Electabuzz"],
    subtypes=["Basic"],
    collector_number=46,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=125,
    abilities=[
        Attack(
            title="Lightning Rod",
            game_text="Choose 1 of your opponent's Pok\u00e9mon and put a Lightning Rod marker on it. (A Pok\u00e9mon can have only 1 Lightning Rod marker on it at a time.)",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=lightning_rod,
        ),
        Attack(
            title="Lightning Bolt",
            game_text="This attack does 20 damage to any Pok\u00e9mon with a Lightning Rod marker on it. Apply Weakness and Resistance.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=10,
            effect=lightning_bolt,
        ),
    ],
)

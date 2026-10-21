from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="712a10ce-132a-5fe9-915c-5d7da6d98786",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NidokingBREAK.Name",
    display_name="Nidoking BREAK",
    searchable_by=["Nidoking BREAK", "BREAK", "NidokingBREAK"],
    subtypes=["BREAK"],
    collector_number=46,
    set_code="XY12",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoking.Name",
    family_id=32,
    abilities=[
        Attack(
            title="Toxic Drill",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned. Put 2 damage counters instead of 1 on that Pok\u00e9mon between turns.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=condition_attack(SpecialConditions.POISONED, counters=2),
        ),
    ],
)
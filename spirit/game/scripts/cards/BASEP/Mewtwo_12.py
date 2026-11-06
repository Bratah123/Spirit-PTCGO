from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.ecard import energy_control


card = PokemonCardDef(
    guid="7933f337-aecf-5fdb-8ff6-e1a2c3490d22",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mewtwo.Name",
    display_name="Mewtwo",
    searchable_by=["Mewtwo", "Basic", "Mewtwo"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=150,
    abilities=[
        Attack(
            title="Energy Control",
            game_text="Flip a coin. If heads, choose a basic Energy card attached to 1 of your opponent's Pok\u00e9mon and attach it to another of your opponent's Pok\u00e9mon of your choice.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=energy_control,
        ),
        Attack(
            title="Telekinesis",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 30 damage to that Pok\u00e9mon. Don't apply Weakness and Resistance for this attack. (Any other effects that would happen after applying Weakness and Resistance still happen.)",
            cost={PokemonTypes.PSYCHIC: 3},
            effect=snipe_attack(30, pool='any', apply_modifiers=False, prompt="Choose 1 of your opponent's Pokémon"),
        ),
    ],
)

from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import feint_attack, mean_look


card = PokemonCardDef(
    guid="ee10d2d4-ae84-5618-aec0-e02cb301056b",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Murkrow.Name",
    display_name="Murkrow",
    searchable_by=["Murkrow", "Basic", "Murkrow"],
    subtypes=["Basic"],
    collector_number=24,
    set_code="NEO1",
    rarity=Rarities.Rare,
    hp=50,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=198,
    abilities=[
        Attack(
            title="Mean Look",
            game_text="The Defending Pok\u00e9mon can't retreat as long as Murkrow remains your Active Pok\u00e9mon. (Benching or evolving either Pok\u00e9mon ends this effect.)",
            cost={PokemonTypes.DARKNESS: 1},
            effect=mean_look,
        ),
        Attack(
            title="Feint Attack",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 20 damage to that Pok\u00e9mon. This attack's damage isn't affected by Weakness, Resistance, Pok\u00e9mon Powers, or any other effects on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            effect=feint_attack,
        ),
    ],
)

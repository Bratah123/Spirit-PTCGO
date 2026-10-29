from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm12 import chaotic_order_gx, violent_appetite, violent_appetite_condition

card = PokemonCardDef(
    guid="46360c0f-7e96-50a3-9d39-75024a11a9fa",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NaganadelGuzzlordGX.Name",
    display_name="Naganadel & Guzzlord-GX",
    searchable_by=["Naganadel & Guzzlord-GX", "Basic", "TAG TEAM", "GX", "Ultra Beast", "NaganadelGuzzlordGX"],
    subtypes=["Basic", "TAG TEAM", "GX", "Ultra Beast"],
    collector_number=260,
    set_code="SM12",
    rarity=Rarities.RareRainbow,
    hp=280,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    family_id=799,
    abilities=[
        Ability(
            title="Violent Appetite",
            game_text="Once during your turn (before your attack), you may discard a Pok\u00e9mon from your hand. If you do, heal 60 damage from this Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            condition=violent_appetite_condition,
            effect=violent_appetite,
        ),
        Attack(
            title="Jet Pierce",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=180,
        ),
        Attack(
            title="Chaotic Order-GX",
            game_text="Turn all of your Prize cards face up. (Those Prize cards remain face up for the rest of the game.) If this Pok\u00e9mon has at least 1 extra Psychic Energy and 1 extra Darkness Energy attached to it (in addition to this attack's cost), take 2 Prize cards. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=chaotic_order_gx,
        ),
    ],
)
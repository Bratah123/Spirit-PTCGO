from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import mill_attack

card = PokemonCardDef(
    guid="335d48e9-4d6e-52be-aaa4-19ca779b2fbd",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Krokorok.Name",
    display_name="Krokorok",
    searchable_by=["Krokorok", "Stage 1", "Krokorok"],
    subtypes=["Stage 1"],
    collector_number=79,
    set_code="CZ",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sandile.Name",
    family_id=552,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
        ),
        Attack(
            title="Dredge Up",
            game_text="Discard the top 3 cards of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=mill_attack(3),
        ),
    ],
)
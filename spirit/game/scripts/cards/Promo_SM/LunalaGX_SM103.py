from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.gum import break_burn


card = PokemonCardDef(
    guid="c3eda48f-059b-511a-9737-70daffdcced0",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LunalaGX.Name",
    display_name="Lunala-GX",
    searchable_by=["Lunala-GX", "Stage 2", "GX", "LunalaGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=103,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=230,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cosmoem.Name",
    family_id=792,
    abilities=[
        Attack(
            title="Glide",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Lunar Javelin",
            game_text="Discard 2 Psychic Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 2},
            damage=200,
            effect=break_burn,
        ),
        Attack(
            title="Requiem-GX",
            game_text="(You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 3, PokemonTypes.COLORLESS: 1},
            damage=250,
            effect=None,
        ),
    ],
)
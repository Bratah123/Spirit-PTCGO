from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import protect_next_turn
from spirit.game.card_effects.pokemon import shred


card = PokemonCardDef(
    guid="2c42b9d0-5709-5e8c-8693-f9f908e191d5",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KommooGX.Name",
    display_name="Kommo-o-GX",
    searchable_by=["Kommo-o-GX", "Stage 2", "GX", "KommooGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=71,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=240,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hakamoo.Name",
    family_id=782,
    abilities=[
        Attack(
            title="Adamantine Press",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=protect_next_turn(reduce=30),
        ),
        Attack(
            title="Shred",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=shred,
        ),
        Attack(
            title="Ultra Uppercut-GX",
            game_text="(You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=240,
            effect=None,
        ),
    ],
)
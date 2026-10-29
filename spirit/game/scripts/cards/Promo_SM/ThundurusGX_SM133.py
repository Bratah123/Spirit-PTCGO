from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_lightning_energy
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.card_effects.smp import thundering_hurricane_gx


card = PokemonCardDef(
    guid="2c8f9ca4-0c36-5ddb-bfa2-48a06209792c",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ThundurusGX.Name",
    display_name="Thundurus-GX",
    searchable_by=["Thundurus-GX", "Basic", "GX", "ThundurusGX"],
    subtypes=["Basic", "GX"],
    collector_number=133,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=642,
    abilities=[
        Attack(
            title="Charge",
            game_text="Search your deck for a Lightning Energy card and attach it to this Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=search_attach_energy(predicate=is_lightning_energy, count=1, to_self=True),
        ),
        Attack(
            title="Electric Ball",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=140,
        ),
        Attack(
            title="Thundering Hurricane-GX",
            game_text="Flip 4 coins. This attack does 100 damage for each heads. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=100,
            damage_operator="x",
            effect=thundering_hurricane_gx,
        ),
    ],
)
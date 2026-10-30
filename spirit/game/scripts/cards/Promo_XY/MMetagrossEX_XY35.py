from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_energy


card = PokemonCardDef(
    guid="97cdca0d-9112-50db-a6f3-62a8b3ab570e",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MMetagrossEX.Name",
    display_name="M Metagross-EX",
    searchable_by=["M Metagross-EX", "MEGA", "EX", "MMetagrossEX"],
    subtypes=["MEGA", "EX"],
    collector_number=35,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=220,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MetagrossEX.Name",
    family_id=376,
    abilities=[
        Attack(
            title="Gatling Slug",
            game_text="This attack does 10 more damage for each Metal Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=130,
            damage_operator="+",
            effect=damage_per(count_energy('self', energy_type=PokemonTypes.METAL), 10, base=130),
        ),
    ],
)
from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack
from spirit.game.card_effects.attacks_common import damage_per, count_bench


card = PokemonCardDef(
    guid="407b225d-4a96-5f64-bb4b-a02336dc918c",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AudinoEX.Name",
    display_name="Audino-EX",
    searchable_by=["Audino-EX", "Basic", "EX", "AudinoEX"],
    subtypes=["Basic", "EX"],
    collector_number=84,
    set_code="XY10",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=531,
    abilities=[
        Attack(
            title="Drain Slap",
            game_text="Heal 20 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=heal_attack(20),
        ),
        Attack(
            title="Do the Wave",
            game_text="This attack does 10 more damage for each of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=damage_per(count_bench('mine'), 10, base=60),
        ),
    ],
)
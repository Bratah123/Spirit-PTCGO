from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import gust_attack
from spirit.game.card_effects.attacks_common import bonus_if, has_damage


card = PokemonCardDef(
    guid="730d76e3-01e2-52f2-bfaf-5d171f8094cd",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanPersian.Name",
    display_name="Alolan Persian",
    searchable_by=["Alolan Persian", "Stage 1", "AlolanPersian"],
    subtypes=["Stage 1"],
    collector_number=79,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanMeowth.Name",
    family_id=52,
    abilities=[
        Attack(
            title="Taunt",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with their Active Pok\u00e9mon.",
            cost={},
            effect=gust_attack(),
        ),
        Attack(
            title="Claw Rend",
            game_text="If your opponent's Active Pok\u00e9mon already has any damage counters on it, this attack does 30 more damage.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            damage_operator="+",
            effect=bonus_if(has_damage(), 30),
        ),
    ],
)
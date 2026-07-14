from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, condition_bonus_attack

card = PokemonCardDef(
    guid="0581fc36-1674-5b28-90f6-5dcbc2d95d70",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ToxtricityV.Name",
    display_name="Toxtricity V",
    searchable_by=["Toxtricity V", "Basic", "V", "ToxtricityV"],
    subtypes=["Basic", "V"],
    collector_number=182,
    set_code="SWSH2",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=849,
    abilities=[
        Attack(
            title="Poison Jab",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
        Attack(
            title="Electric Riot",
            game_text="If your opponent's Active Pok\u00e9mon is Poisoned, this attack does 90 more damage.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator="+",
            effect=condition_bonus_attack(90, SpecialConditions.POISONED),
        ),
    ],
)
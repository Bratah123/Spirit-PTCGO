from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import AbilityTypes, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.ex import pickup_three, quick_attack_bonus, thick_skin_passive

card = PokemonCardDef(
    guid="61cd2c79-b036-53c7-8851-8d9351b7f73f",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raticate.Name",
    display_name="Raticate",
    searchable_by=["Raticate", "Stage 1", "Raticate"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="EX6",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rattata.Name",
    family_id=19,
    abilities=[
        Ability(
            title="Thick Skin",
            game_text="Raticate can't be affected by any Special Conditions.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=thick_skin_passive(),
        ),
        Attack(
            title="Pickup",
            game_text="Search your discard pile for a Basic Pok\u00e9mon (or Evolution card), a Trainer card, and an Energy card. Show them to your opponent and put them into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=pickup_three(),
        ),
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 40 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=quick_attack_bonus(10, 40),
        ),
    ],
)
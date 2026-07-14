from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.support_common import heal_targets

card = PokemonCardDef(
    guid="57333162-5dc9-5e5c-b4e3-3f5292ab3e8a",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Indeedee.Name",
    display_name="Indeedee",
    searchable_by=["Indeedee", "Basic", "Indeedee"],
    subtypes=["Basic"],
    collector_number=88,
    set_code="SWSH2",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=876,
    abilities=[
        Attack(
            title="Replenish Time",
            game_text="Heal 30 damage from each of your Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=heal_targets(30, "each_own"),
        ),
        Attack(
            title="Psybeam",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)

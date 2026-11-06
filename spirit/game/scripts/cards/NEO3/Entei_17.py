from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import (
    discard_energy_per_tails,
    legendary_body_discard_trainers,
    legendary_body_passive,
)


card = PokemonCardDef(
    guid="a8aa24a3-0ea8-5bd6-81ad-9ee17eb52979",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Entei.Name",
    display_name="Entei",
    searchable_by=["Entei", "Basic", "Entei"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="NEO3",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    family_id=244,
    abilities=[
        Ability(
            title="Legendary Body",
            game_text="As long as Entei is your Active Pok\u00e9mon, Entei and Energy cards attached to it aren't affected by effects from Trainer cards other than Stadium cards. As long as this Power is active, discard any Trainer cards attached to Entei. (This power works even if Entei is Asleep, Confused, or Paralyzed.)",
            ability_type=AbilityTypes.POKE_POWER,
            passive=legendary_body_passive,
            trigger=(Triggers.ON_MOVE_TO_ACTIVE, Triggers.BETWEEN_TURNS),
            effect=legendary_body_discard_trainers,
        ),
        Attack(
            title="Mega Flame",
            game_text="Flip 2 coins. For each tails, discard 1 Fire Energy card from Entei, if it has any.",
            cost={PokemonTypes.FIRE: 3},
            damage=50,
            effect=discard_energy_per_tails(2, PokemonTypes.FIRE),
        ),
    ],
)
